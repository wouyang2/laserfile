# process directory
## The Process directory contains four python files
* ### order_reverse.py: reverse the order of two points in the sublist. (not necessary when points are arranged in order)

* ### plot_segment.py: Interpolates between given points with a consistent spacing. If the input list contains only two points, it linearly interpolates between them. If the input list contains more than two points, it uses B-spline interpolation. Then it project the 3D coordinates onto a 2D plane based on the normal vector of the shape. Lastly, upscale to the ilda coordinate system and output to a json file in specific format. 

	    each point is formatted as: 
	    {
            "segment": 0,
            "x": -5772.550179748316,
            "y": -30000.0,
            "color": 0,
            "blanking": true
        }

* ### *Path2.py: Insert interpolated points between two points with different segment values, blanking of every interpolated points is set to true.

* ### *process.py: Assemble all the functions in all other three python file, generate a json file as outputs

## Usage: In the process directory, open process.py file, in the process("input file path", "output file path") function at the very bottom, change the input file, output file path accordingly.

    Ex: process("/Users/mrweilin/Desktop/Research/New_floor/revise_new_floor.json", "/Users/mrweilin/Desktop/Research/New_floor/final_new_floor.json")   

<br/>

# laser directory
## laser-dac-master/packages/ilda-reader
* ### test.ts: read in a ilda file and convert it to array of point (use "> output.json" to store the output to a json file)
    
        const buffer = fs.readFileSync('file.ild');

## laser-dac-master/packages/ilda-writer
* ### test.ts: read in a json file and convert it to a ilda file 
    
        const data = fs.readFileSync('input.json', 'utf8');
        fs.writeFileSync('output.ild', b);
