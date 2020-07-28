fn main() {
	let bits = BitArray::new(21);
	println!("{:#b}", 21);
	println!("{}", bits.get(6)); 
}


struct BitArray {
	bits: u8
}

impl BitArray {
	fn new(init : u8) -> BitArray {
		BitArray {
			bits : init 
		}			
	}
	fn get(&self,index : u8) -> bool {
		assert!(index < 8);
		let baseValue = 1 << index;
		let getSpecficBit  = (self.bits & baseValue) >> index;
		getSpecficBit == 1
	}	
	fn set(&mut self, index : u8, value : bool) {
		assert!(index < 8);
		let baseValue = 1 << index;
		self.bits = if value {
			//this uses "OR" operation on it 
			self.bits | baseValue
		} else {
			self.bits & !baseValue
		
		}
	}
}