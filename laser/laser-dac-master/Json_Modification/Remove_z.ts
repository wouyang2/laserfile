import * as fs from 'fs';

interface Point {
    x: number;
    y: number;
    z?: number;  // Make the z-coordinate optional
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

const removeZCoordinate = (inputPath: string, outputPath: string) => {
    // Read and parse the file content
    const rawData = fs.readFileSync(inputPath, 'utf-8');
    const data: DataObject[] = JSON.parse(rawData);

    // Remove the z-coordinate from each point
    data.forEach(obj => {
        obj.points.forEach(point => {
            delete point.z;
        });
    });

    // Write the modified content back to the output file
    fs.writeFileSync(outputPath, JSON.stringify(data, null, 4));
}

// Usage example
removeZCoordinate('/Users/mrweilin/Desktop/Research /Green_Dented_Rec_t5.json', 'Green_Dented_Rec_t5_no_z.json');
