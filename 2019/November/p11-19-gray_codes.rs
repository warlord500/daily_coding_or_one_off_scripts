
/* 
# Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. 
# Gray code is common in hardware so that we don't see temporary spurious values during transitions.

# Given a number of bits n, generate a possible gray code for it.

# For example, for n = 2, one gray code would be [00, 01, 11, 10].
 */
fn generate_gray_code(numberOfBits : u8) -> Vec<u32> {
   //in practice, you would run out of memory long before you get to 32 bits.
   //however in theory this code fails to work correctly above 32
   assert!(numberOfBits <= 32);  
   if numberOfBits == 0 { 
		return Vec::new() 
   } 
	let mut sequences = vec![1,0];
	for i in 0..numberOfBits {
		for j in (0..sequences.len()).rev() {
			let nextValue = sequences[j] + 1 << i;
			sequences.push(nextValue) 
		}

	}
   sequences
}

fn main() {
	print!("hello world");
	for item in generate_gray_code(3) {
		println!("{:#08b} {}",item,item);
	}
}