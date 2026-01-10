#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def convert_to_xa(input_dir="audio", output_dir="xa_output"):
    """Convierte archivos de audio a formato XA"""
    
    # Crear directorio de salida
    Path(output_dir).mkdir(exist_ok=True)
    
    # Extensiones soportadas
    audio_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in audio_extensions:
            output_file = Path(output_dir) / f"{file_path.stem}.xa"
            
            print(f"Convirtiendo: {file_path} -> {output_file}")
            
            # Usar ffmpeg para conversión
            command = [
                'ffmpeg', '-i', str(file_path),
                '-acodec', 'adpcm_ima_ea_xas',
                '-ar', '37800',
                '-ac', '2',
                str(output_file)
            ]
            
            try:
                subprocess.run(command, check=True)
                print(f"✓ Conversión exitosa")
            except subprocess.CalledProcessError as e:
                print(f"✗ Error convirtiendo {file_path}: {e}")

if __name__ == "__main__":
    convert_to_xa()
