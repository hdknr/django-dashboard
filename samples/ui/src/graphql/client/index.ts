import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client'
import { setContext } from '@apollo/client/link/context';
import { GRAPHQL_URL, GRAPHQL_URL_WS } from '../../settings';
import { WebSocketLink } from '@apollo/client/link/ws';


const cache = new InMemoryCache();
const httpLink = createHttpLink({
    uri: GRAPHQL_URL
});


const authLink = setContext(async (_, { headers }) => {
    return await fetch(GRAPHQL_URL, {
        method: 'GET',
        mode: 'cors',
        credentials: 'include',
    })
        .then((response) => {
            const csrfToken = response.headers.get('X-CSRFToken');
            return {
                mode: 'cors',
                credentials: 'include',
                headers: {
                    ...headers,
                    'X-CSRFToken': csrfToken,
                },
            };
        })
        .catch((error) => {
            console.log({ error });
        });
});

const wslink = new WebSocketLink({
    uri: GRAPHQL_URL_WS,
    options: {
        reconnect: true
    }
})

// const link = authLink.concat(httpLink);
const link = wslink;


export const client = new ApolloClient({
    link, cache
});