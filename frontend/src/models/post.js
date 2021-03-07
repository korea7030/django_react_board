import { types, flow, onSnapshot, cast, getParent } from 'mobx-state-tree';
import bookApi from '../apis/bookApi';
import User from './user';


const Comment = types.model('Comment', {
    id: types.integer,
    comment: types.string,
    parent: types.identifier,
    user: types.safeReference(User),
});

const AttachmentFile = types.model('AttachmentFile', {
    id: types.integer,
    user: types.safeReference(User),
});

const Post = types.model('Post', {
    id: types.integer,
    title: types.string,
    content: types.maybe(types.string),
    author: types.safeReference(User),
    hit: types.integer,
    comments: types.array(Comment),
    files: types.array(AttachmentFile)
}).actions(self => {
    return {
        load: flow(function* () {
            // console.log('parent : ', getParent(self, 1));
            // const {id: postID} = getParent(self, 1);
            const {comments} = yield bookApi.getComment(self.id);

            self.comments = cast(comments);

            // onSnapshot(self, self.save);
        }),
        afterCreate() {
            self.load();
        }
    }
});

export default Post;