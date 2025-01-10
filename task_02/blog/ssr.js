export async function getServerSideProps(context) {
    const { id } = context.query;
    const res = await fetch(`http://localhost:3000/api/blog/${id || 1}`);
    const blog = await res.json();

    return {
        props: { blog },
    };
}

const BlogPostSSR = ({ blog }) => {
    if (blog.error) return <p>{blog.error}</p>;

    return (
        <div>
            <h1>{blog.title}</h1>
            <p>{blog.content}</p>
        </div>
    );
};

export default BlogPostSSR;
