export async function getStaticProps() {
    const res = await fetch("http://localhost:3000/api/blog");
    const blogs = await res.json();

    return {
        props: { blogs },
    };
}

const HomePage = ({ blogs }) => (
    <div>
        <h1>Blog</h1>
        <ul>
            {Object.entries(blogs).map(([id, blog]) => (
                <li key={id}>
                    <a href={`/blog/${id}`}>{blog.title}</a>
                </li>
            ))}
        </ul>
    </div>
);

export default HomePage;
