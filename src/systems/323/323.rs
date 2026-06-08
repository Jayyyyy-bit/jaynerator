use std::io::{self, Read, Write};
use std::fs;

pub struct 323 {
    // TODO: add your fields here
}

impl 323 {
    pub fn new() -> Self {
        323 {
            // TODO: initialize fields
        }
    }

    pub fn run(&self) -> Result<(), Box<dyn std::error::Error>> {
        // TODO: add your core logic here
        println!("323 running...");
        Ok(())
    }

    pub fn read_file(&self, path: &str) -> Result<String, io::Error> {
        fs::read_to_string(path)
    }

    pub fn write_file(&self, path: &str, content: &str) -> Result<(), io::Error> {
        let mut file = fs::File::create(path)?;
        file.write_all(content.as_bytes())?;
        Ok(())
    }
}

fn main() {
    let tool = 323::new();
    if let Err(e) = tool.run() {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }
}