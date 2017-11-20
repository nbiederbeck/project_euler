// The prime factors of 13195 are 5, 7, 13, 29.
// What is the largest prime factor of the number 600851475143 ?
fn main() {
    const NUMBER_OF_INTEREST: u32 = 600851475143;
    const NUMBER_TEST: u32 = 13195;
    const SOLUTION_TEST: (u32, u32, u32, u32) = (9, 7, 13, 29);

    let prime = primes(NUMBER_TEST);

    println!("Hello, {}!", prime);
}

fn primes(max_number: u32) -> u32 {
    let mut primes = [2, 3];
    primes[0]
}
