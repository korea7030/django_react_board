import { types, flow } from 'mobx-state-tree';
import BookApi from '../apis/bookApi';
import Post from '../models/post';

const BoardStore = types.model('BoardStore', {
    posts: types.array(Post)
}).actions(self => {
    return {
        load: flow(function* () {
            self.posts = yield BookApi.getPostAll();
        }),
        afterCreate() {
            self.load();
        }
    };
});

export default BoardStore;