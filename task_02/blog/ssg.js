export async function getStaticPaths() {
    const res = await fetch(`http://localhost:3000/api/blog`);
    const blogs = await res.json();

    const paths = Object.keys(blogs).map((id) => ({
        params: { id },
    }));

    return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
    const res = await fetch(`http://localhost:3000/api/blog/${params.id}`);
    const blog = await res.json();

    return {
        props: { blog },
    };
}

const BlogPostSSG = ({ blog }) => (
    <div>
        <h1>{blog.title}</h1>
        <p>{blog.content}</p>
    </div>
);

export default BlogPostSSG;
