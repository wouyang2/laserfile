import { toByteArray } from './src';
import * as fs from 'fs';

const data = fs.readFileSync('/Users/mrweilin/Desktop/Research/curved_pipe.json', 'utf8');
const json = JSON.parse(data);

const byteArray = toByteArray(json);

const b = new Buffer(byteArray);
fs.writeFileSync('Pipe_line.ild', b);
console.log("SUCCESS!!")