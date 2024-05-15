export type ByteArray = Uint8Array | number[];

export class ArrayReader {
  bytes: ByteArray;
  length: number;
  position = 0;

  constructor(bytes: ByteArray) {
    this.bytes = bytes;
    this.length = this.bytes.length;
  }

  seek(p: number) {
    this.position = p;
  }

  eof() {
    return this.position >= this.length;
  }

  readString(length: number) {
    var s = '';
    for (var i = 0; i < length; i++) {
      var b0 = this.readByte();
      if (b0 > 0 && b0 < 0x7f) s += String.fromCharCode(b0);
    }
    return s.trim();
  }

  readByte() {
    var b = this.bytes[this.position];
    this.position++;
    return b;
  }

  readShort() {
    var b0 = this.readByte();
    var b1 = this.readByte();
    return (b0 << 8) + b1;
  }

  readSignedShort() {
    var b0 = this.readByte();
    var b1 = this.readByte();
    var s = (b0 << 8) + b1;
    if (s > 32768) s = -(65535 - s);
    return s;
  }

  readLong() {
    var b0 = this.readByte();
    var b1 = this.readByte();
    var b2 = this.readByte();
    var b3 = this.readByte();
    return b3 + (b2 << 8) + (b1 << 16) + (b0 << 24);
  }

  
}
