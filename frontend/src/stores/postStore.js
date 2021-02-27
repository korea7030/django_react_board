import { action, observable, makeObservable, computed } from "mobx";
import BookApi from '../apis/bookApi';

class PostStore {
    posts = [];

    constructor() {
        makeObservable(this, {
            posts: observable,
            totalPosts: computed,
            createPost: action,
            updatePost: action,
            deletePost: action,
            detailPost: action,
        });
    }

    get totalPosts() {
        return this.posts.length;
    }

    async getPost() {
        return await BookApi.getPostAll();
    }

    async detailPost(postId) {
        return await BookApi.detailPost(postId);
    }

    async createPost(post = { title: "", content: "", author: null }) {
        // call api
        return await BookApi.createPost(post);
    }

    async updatePost(postId, data) {
        // call api
        return await BookApi.updatePost(postId, data);
    }

    async deletePost(postId) {
        // call api
        return await BookApi.deletePost(postId);
    }
}

export default PostStore;