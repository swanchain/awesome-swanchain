import {
    createRouter,
    createWebHistory,
    createWebHashHistory
} from 'vue-router'
const home = () =>
    import ("@/components/Home");
const dashboard = () =>
    import ("@/views/dashboard/index");
const jsonViewer = () =>
    import ("@/views/dashboard/jsonViewer/index");

const routes = [{
        path: '/',
        redirect: '/dashboard'
    },
    {
        path: '/',
        component: home,
        children: [{
            path: '/dashboard',
            component: dashboard,
            children: [{
                    path: '/dashboard',
                    redirect: '/jsonViewer'
                },
                {
                    path: '/jsonViewer',
                    name: 'jsonViewer',
                    component: jsonViewer
                }
            ]
        }, ]
    },
    {
        path: '/:pathMatch(.*)*',
        redirect: '/'
    }
]

const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    routes
})

export default router