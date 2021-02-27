import PostStore from "./postStore";
import UserStore from "./userStore";

const rootStore = () => {
    return {PostStore, UserStore}
};

export default rootStore;