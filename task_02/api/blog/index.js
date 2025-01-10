export default function handler(req, res) {
    const mockBlogData = {
        1: { title: "Next.js Basics", content: "Learn the fundamentals of Next.js." },
        2: { title: "API Routes", content: "How to use API routes in Next.js." },
    };

    res.status(200).json(mockBlogData);
}
