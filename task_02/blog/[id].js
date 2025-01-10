import { useRouter } from "next/router";
import { useEffect, useState } from "react";

const BlogPost = () => {
    const { query } = useRouter();
    const { id } = query;
    const [blog, setBlog] = useState(null);

    useEffect(() => {
        if (id) {
            fetch(`/api/blog/${id}`)
                .then((res) => res.json())
                .then((data) => setBlog(data));
        }
    }, [id]);

    if (!blog) return <p>Loading...</p>;
    if (blog.error) return <p>{blog.error}</p>;

    return (
        <div>
            <h1>{blog.title}</h1>
            <p>{blog.content}</p>
        </div>
    );
};

export default BlogPost;
