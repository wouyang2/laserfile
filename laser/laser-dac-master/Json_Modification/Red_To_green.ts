import * as fs from 'fs';

interface Point {
    x: number;
    y: number;
    z: number;
    r: number;
    g: number;
    b: number;
    blanking: boolean;
}

interface DataObject {
    name: string;
    type: number;
    points: Point[];
}

const modifyPoints = (inputPath: string, outputPath: string) => {
    // Read and parse the file content
    const rawData = fs.readFileSync(inputPath, 'utf-8');
    const data: DataObject[] = JSON.parse(rawData);

    // Modify the points as per the requirement
    data.forEach(obj => {
        obj.points.forEach(point => {
            point.g = 128;
            point.r = 0;
            point.b = 128;
        });
    });

    // Write the modified content back to the output file
    fs.writeFileSync(outputPath, JSON.stringify(data, null, 4));
}

// Usage example
modifyPoints('/Users/mrweilin/Desktop/Research /Green_pikachu_reader_t5.json', 'Green_pikachu_reader_t5.json');
