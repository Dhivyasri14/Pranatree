import { useState, useEffect } from 'react';

export default function Home() {
    const [greeting, setGreeting] = useState('Loading...');

    const fetchGreeting = async () => {
        try {
            const response = await fetch(`${window.location.origin}/api/greet`);
            const data = await response.json();
            setGreeting(data.message);
        } catch (error) {
            console.error('Error fetching greeting:', error);
            setGreeting('Failed to fetch greeting.');
        }
    };

    useEffect(() => {
        fetchGreeting();
    }, []);

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>{greeting}</h1>
        </div>
    );
}
