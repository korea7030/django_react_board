import http from '../http-common';


class BookApi {
    getPostAll = async () => {
        const response = await http.get("boards/post");
        return response['data'];
    };
    
    createPost = async(data) => {
        return await http.post("post", data);
    }
    
    detailPost = async(id) => {
        return await http.get(`boards/post/${id}`);
    }
    
    updatePost = async(id, data) => {
        return await http.put(`boards/post/${id}`, data);
    }
    
    deletePost = async(id) => {
        return await http.delete(`boards/post/${id}`);
    }

    getComment = async(id) => {
        const response = await http.get(`boards/view/comment/${id}`);
        return response['data']
    }
}

export default new BookApi();