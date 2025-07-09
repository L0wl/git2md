from .base import BaseConverter
from __future__ import annotations
from pathlib import Path

class BinaryConverter(BaseConverter):
    """Converter that outputs a hexdump for binary files up to 1MB."""

    max_size: int = 1 * 1024 * 1024  # 1MB
    aliases: list[str] = []

    def supports(self, file_path: Path) -> bool:  # type: ignore[override]
        if file_path.stat().st_size > self.max_size:
            return False
        try:
            with file_path.open("rb") as f:
                chunk = f.read(1024)
            if b"\x00" in chunk:
                return True
            chunk.decode("utf-8")
            return False
        except UnicodeDecodeError:
            return True
        except Exception:
            return False

    def convert(self, file_path: Path) -> str:
        data = file_path.read_bytes()
        lines: list[str] = []
        for i in range(0, len(data), 16):
            chunk = data[i : i + 16]
            hex_bytes = " ".join(f"{b:02x}" for b in chunk)
            ascii_repr = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
            lines.append(f"{i:08x}  {hex_bytes:<48}  {ascii_repr}")
        return "\n".join(lines)

    def get_language(self, file_path: Path) -> str | None:  # type: ignore[override]
        return "text"


converter = BinaryConverter()