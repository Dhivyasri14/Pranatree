export default async function handler(req, res) {
    try {
        const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
            },
            body: JSON.stringify({
                model: 'llama3-8b-8192',
                messages: [{ role: 'user', content: 'Say a friendly greeting!' }],
                max_tokens: 10,
            }),
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }
        
        const data = await response.json();
        const message = data.choices[0]?.message?.content.trim() || 'No response received';
        res.status(200).json({ message });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: error.message });
    }
}
