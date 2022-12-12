fn main() {
	let num = 0b01111010u8;
	//should run some code to accept a number.
	//either a binary or 10 radix
	
    	
    println!("{:#b}",evenBitSwap(num));


    //full test 
    for i in (0..=255) {
        
       println!("{:#b} : {:#b}",i,evenBitSwap(i));
    }
}

fn evenBitSwap (number : u8) -> u8 {
		//well we know that we would have 8 bits and have to do 4 swaps?
		// lets see we have ands,ors,xors,rotates,shifts, 
		// maybe some kind of asm command? 
		//lets check
        //i guess probably not most efficent way to do this but we could 
        //extract each bit at time. 
    /*let mut bitArray = [0; 8];
    for i in (0..8) {
        bitArray[i] = (number >> i) & 0b00000001u8;
    }
    // uhh now swap evens and odds?
    let mut outNum = 0;
    for i in (0..8) {
        
            outNum = outNum | (bitArray[if(i%2==0){i+1}else{i-1}] << i); 
    }*/ 
    //above is my slow, but reliable probably easy to understand
    //this is my faster single line of code. 
    let oddBits =  0b01010101;
    let  evenBits = 0b10101010;
    let outNum = ((number & oddBits) << 1) | ((number & evenBits) >> 1);  
        
        outNum
}
