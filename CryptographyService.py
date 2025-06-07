import base64

class CryptographyService:    
    def encode_base64(input_string: str) -> str:
        input_bytes = input_string.encode('utf-8')
        base64_bytes = base64.b64encode(input_bytes)
        return base64_bytes.decode('utf-8')
    
    def decode_base64(base64_string: str) -> str:
        base64_bytes = base64_string.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('utf-8')
