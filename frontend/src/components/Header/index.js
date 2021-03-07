import {AppBar, Grid, Select, Toolbar, Typography, Box, FormControl} from '@material-ui/core';

function Header() {
    return (
        <AppBar position="static">
            <Toolbar variant="dense">
                <Grid container justify="space-between" alignItems="center">
                <Grid item>
                    <Box display="flex" alignItems="center" p={1}>
                    <Typography variant="h6" color="inherit">
                        Board
                    </Typography>
                    </Box>
                </Grid>
                {/* <Grid item>
                    <User user={users?.me}/>
                </Grid> */}
                </Grid>
            </Toolbar>
        </AppBar>
    )
}

export default Header;