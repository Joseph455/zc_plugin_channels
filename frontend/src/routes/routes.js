import { Switch, Route } from 'react-router-dom'
import Home from '../components/home/Home'
import Admin from '../components/admin/index'
import CreateChannel from '../components/createChannel/index'
import MessageBoardIndex from '../components/MessageBoard/MessageBoardIndex'
import ChannelDetailsAndSetting from '../components/channelDetailsAndSetting/index'
import TempSidebar from '../components/TempSidebar/index'
import { Box, HStack } from '@chakra-ui/layout'

const routes = () => {
  return (
    <Switch>
      <HStack>
        <TempSidebar />

        <Route exact path='/'>
          <Home />
        </Route>
        <Route path='/create-channel'>
          <CreateChannel />
        </Route>
        <Route path='/admin'>
          <Admin />
        </Route>
        <Route path='/message-board'>
          <MessageBoardIndex />
        </Route>
        <Route path='/channel-detail'>
          <ChannelDetailsAndSetting />
        </Route>
      </HStack>
    </Switch>
  )
}

export default routes
