import http from '../http-common';

const getPostAll = async () => {
    return await http.get("post");
};

const createPost = async(data) => {
    return await http.post("post", data)
}

const detailPost = async(id) => {
    return await http.get(`post/${id}`);
}

