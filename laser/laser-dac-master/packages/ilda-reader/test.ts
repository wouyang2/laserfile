import { fromByteArray } from './src';
import * as fs from 'fs';

const buffer = fs.readFileSync('/Users/mrweilin/Desktop/Research/pipe_line/curved_pipe_11.ild');
const output = fromByteArray(new Uint8Array(buffer));

//console.log(output);

console.log(JSON.stringify(output, null, 2));