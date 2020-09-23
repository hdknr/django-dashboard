import React from 'react';
import { useLatestNoticeSubscription } from '../../graphql';


export const Top: React.FunctionComponent = () => {
    // https://www.apollographql.com/docs/react/data/subscriptions/#usesubscription-api-reference
    const {
        data, loading, error,
    } = useLatestNoticeSubscription({ variables: { arg1: '', arg2: '' } });

    return (
        <div>
            <h4>Top</h4>
            <div>
                <span>{data?.latestnotice?.title}</span>

                <ul>
                    {data?.latestnotice?.notices?.map((notice, index) => (
                        <li>
                            {notice?.message?.message}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};
