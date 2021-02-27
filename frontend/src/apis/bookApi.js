import http from '../http-common';


export default class BookApi {
    getPostAll = async () => {
        return await http.get("post");
    };
    
    createPost = async(data) => {
        return await http.post("post", data);
    }
    
    detailPost = async(id) => {
        return await http.get(`post/${id}`);
    }
    
    updatePost = async(id, data) => {
        return await http.put(`post/${id}`, data);
    }
    
    deletePost = async(id) => {
        return await http.delete(`post/${id}`);
    }
}