import { observer } from 'mobx-react-lite';
import {
    List,
    ListItem,
    ListItemText,
    ListItemIcon,
    IconButton,
    ListItemSecondaryAction,
    Box
  } from '@material-ui/core';
import InboxIcon from "@material-ui/icons/Inbox";
import EditIcon from '@material-ui/icons/Edit';
import useStore from '../../hooks/useStore';

const getListStyle = () => ({
    padding: 8,
    minHeight: 500,
});


function Post() {
    const {posts} = useStore();
    return (
       <List style={getListStyle()}>
           {posts?.posts.map(post => {
               return (
                <ListItem
                ContainerComponent="li"
                key={post?.id}
                >
                <ListItemIcon>
                    <InboxIcon />
                </ListItemIcon>
                <ListItemText
                    primary={post?.title}
                    secondary={post?.content}
                />
                <ListItemSecondaryAction>
                    <IconButton>
                    <EditIcon />
                    </IconButton>
                </ListItemSecondaryAction>
                </ListItem> 
               )
            })}
       </List>
    )
}

export default observer(Post);