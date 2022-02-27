import TypingSpeedTest from "@/views/pages/Games/TypingSpeedTest.vue";
import MatchingGame from "@/views/pages/Games/MatchingGame.vue";

const gameRoutes = [
    {
      path: '/code/typing-speed-test',
      name: 'typing-speed-test',
      component: TypingSpeedTest,
      meta: {
        title: 'Typing Speed Test - DanielOnline'
      }
    },
    {
      path: '/code/matching-game',
      name: 'matching-game',
      component: MatchingGame,
      meta: {
        title: 'MatchingGame - DanielOnline'
      }
    }
  ];
  
  export default gameRoutes;