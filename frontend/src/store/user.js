import { types } from 'mobx-state-tree';
import User from '../models/user';

const UserStore = types.model('UserStore', {
    user: types.safeReference(User)
});

export default UserStore;