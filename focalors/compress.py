import zlib

def compress_file(input_file: str, output_file: str):
    """Decompress the given file and write to output_file."""
    with open(input_file, 'rb') as file:
        compressed_data = file.read()
    
    # 압축 해제
    decompressed_data = zlib.decompress(compressed_data)
    
    # 결과를 출력 파일에 저장
    with open(output_file, 'wb') as file:
        file.write(decompressed_data)

    print(f"File decompressed to {output_file}")
