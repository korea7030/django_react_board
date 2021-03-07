import { types } from 'mobx-state-tree';
import UserStore from './user';
import BoardStore from './board';

const RootStore = types.model('RootStore', {
    users: types.optional(UserStore, {}),
    posts: types.optional(BoardStore, {}),
});

export default RootStore;