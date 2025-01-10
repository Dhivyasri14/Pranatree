export default function handler(req, res) {
    const { id } = req.query;
    const mockBlogData = {
        1: { title: "Next.js Basics", content: "Learn the fundamentals of Next.js." },
        2: { title: "API Routes", content: "How to use API routes in Next.js." },
    };

    if (mockBlogData[id]) {
        res.status(200).json(mockBlogData[id]);
    } else {
        res.status(404).json({ error: "Blog not found" });
    }
}
