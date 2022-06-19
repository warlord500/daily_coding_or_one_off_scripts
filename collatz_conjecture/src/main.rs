fn main() {
    println!("Hello, world!");
	//replace these two variables to determine input numbers for routes!
	let min = 1; 
	let max = 33;
	for i in (min..max)	{ // loop thru 1 to 33 
		let route = proccess_number(i); 
		println!("input: {}, stopping time:{} output: {:?}",i,route.len(),route );
	}
	
}
//this computes the route which was used 
fn proccess_number(mut input: u32) -> Vec<u32> {
	if input == 0 || input == 1 {
			return Vec!{1}
	} else {
		//while i know this is recursive the result is the same!
		let mut route = Vec::new(); //a list
		route.push(input);
		while(input != 1){
			if input % 2 == 0 { //even divide odd multiply
				input = input/2;
			} else {
				input= input*3 + 1
			}
			route.push(input);
			
		}

		return route;
		
	}
}