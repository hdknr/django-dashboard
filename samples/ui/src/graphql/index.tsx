import gql from 'graphql-tag';
import * as ApolloReactCommon from '@apollo/react-common';
import * as ApolloReactHooks from '@apollo/react-hooks';
export type Maybe<T> = T | null;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  DateTime: any;
};


export type LatestNotice = {
  __typename?: 'LatestNotice';
  title?: Maybe<Scalars['String']>;
  notices?: Maybe<Array<Maybe<Notice>>>;
};

export type Message = Node & {
  __typename?: 'Message';
  created_at: Scalars['DateTime'];
  updated_at: Scalars['DateTime'];
  id: Scalars['ID'];
  subject: Scalars['String'];
  message?: Maybe<Scalars['String']>;
  url?: Maybe<Scalars['String']>;
  topic?: Maybe<Topic>;
  notice_set: NoticeConnection;
  pk?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
};


export type MessageNotice_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  created_at?: Maybe<Scalars['DateTime']>;
  updated_at?: Maybe<Scalars['DateTime']>;
  read?: Maybe<Scalars['Boolean']>;
  message?: Maybe<Scalars['ID']>;
  user?: Maybe<Scalars['ID']>;
  pk?: Maybe<Scalars['Float']>;
};

export type MessageConnection = {
  __typename?: 'MessageConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<MessageEdge>>;
};

export type MessageEdge = {
  __typename?: 'MessageEdge';
  node?: Maybe<Message>;
  cursor: Scalars['String'];
};

export type MessageNodeSetConnection = {
  __typename?: 'MessageNodeSetConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<MessageNodeSetEdge>>;
  total_count?: Maybe<Scalars['Int']>;
  records?: Maybe<Scalars['Int']>;
};

export type MessageNodeSetEdge = {
  __typename?: 'MessageNodeSetEdge';
  node?: Maybe<Message>;
  cursor: Scalars['String'];
};

export type Node = {
  id: Scalars['ID'];
};

export type Notice = Node & {
  __typename?: 'Notice';
  id: Scalars['ID'];
  created_at: Scalars['DateTime'];
  updated_at: Scalars['DateTime'];
  read: Scalars['Boolean'];
  message?: Maybe<Message>;
  pk?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
};

export type NoticeConnection = {
  __typename?: 'NoticeConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<NoticeEdge>>;
};

export type NoticeEdge = {
  __typename?: 'NoticeEdge';
  node?: Maybe<Notice>;
  cursor: Scalars['String'];
};

export type NoticeNodeSetConnection = {
  __typename?: 'NoticeNodeSetConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<NoticeNodeSetEdge>>;
  total_count?: Maybe<Scalars['Int']>;
  records?: Maybe<Scalars['Int']>;
};

export type NoticeNodeSetEdge = {
  __typename?: 'NoticeNodeSetEdge';
  node?: Maybe<Notice>;
  cursor: Scalars['String'];
};

export type PageInfo = {
  __typename?: 'PageInfo';
  hasNextPage: Scalars['Boolean'];
  hasPreviousPage: Scalars['Boolean'];
  startCursor?: Maybe<Scalars['String']>;
  endCursor?: Maybe<Scalars['String']>;
};

export type Query = {
  __typename?: 'Query';
  topic?: Maybe<Topic>;
  topic_set?: Maybe<TopicNodeSetConnection>;
  message?: Maybe<Message>;
  message_set?: Maybe<MessageNodeSetConnection>;
  notice?: Maybe<Notice>;
  notice_set?: Maybe<NoticeNodeSetConnection>;
};


export type QueryTopicArgs = {
  id: Scalars['ID'];
};


export type QueryTopic_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  parent?: Maybe<Scalars['ID']>;
  code?: Maybe<Scalars['String']>;
  title?: Maybe<Scalars['String']>;
  lft?: Maybe<Scalars['Int']>;
  rght?: Maybe<Scalars['Int']>;
  tree_id?: Maybe<Scalars['Int']>;
  level?: Maybe<Scalars['Int']>;
  pk?: Maybe<Scalars['Float']>;
};


export type QueryMessageArgs = {
  id: Scalars['ID'];
};


export type QueryMessage_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  created_at?: Maybe<Scalars['DateTime']>;
  updated_at?: Maybe<Scalars['DateTime']>;
  subject?: Maybe<Scalars['String']>;
  message?: Maybe<Scalars['String']>;
  url?: Maybe<Scalars['String']>;
  topic?: Maybe<Scalars['ID']>;
  pk?: Maybe<Scalars['Float']>;
};


export type QueryNoticeArgs = {
  id: Scalars['ID'];
};


export type QueryNotice_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  created_at?: Maybe<Scalars['DateTime']>;
  updated_at?: Maybe<Scalars['DateTime']>;
  read?: Maybe<Scalars['Boolean']>;
  message?: Maybe<Scalars['ID']>;
  user?: Maybe<Scalars['ID']>;
  pk?: Maybe<Scalars['Float']>;
};

export type Subscription = {
  __typename?: 'Subscription';
  latestnotice?: Maybe<LatestNotice>;
};


export type SubscriptionLatestnoticeArgs = {
  arg1?: Maybe<Scalars['String']>;
  arg2?: Maybe<Scalars['String']>;
};

export type Topic = Node & {
  __typename?: 'Topic';
  id: Scalars['ID'];
  parent?: Maybe<Topic>;
  code: Scalars['String'];
  title?: Maybe<Scalars['String']>;
  lft: Scalars['Int'];
  rght: Scalars['Int'];
  tree_id: Scalars['Int'];
  level: Scalars['Int'];
  children: TopicConnection;
  message_set: MessageConnection;
  pk?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
  full_code_path?: Maybe<Scalars['String']>;
};


export type TopicChildrenArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  parent?: Maybe<Scalars['ID']>;
  code?: Maybe<Scalars['String']>;
  title?: Maybe<Scalars['String']>;
  lft?: Maybe<Scalars['Int']>;
  rght?: Maybe<Scalars['Int']>;
  tree_id?: Maybe<Scalars['Int']>;
  level?: Maybe<Scalars['Int']>;
  pk?: Maybe<Scalars['Float']>;
};


export type TopicMessage_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  created_at?: Maybe<Scalars['DateTime']>;
  updated_at?: Maybe<Scalars['DateTime']>;
  subject?: Maybe<Scalars['String']>;
  message?: Maybe<Scalars['String']>;
  url?: Maybe<Scalars['String']>;
  topic?: Maybe<Scalars['ID']>;
  pk?: Maybe<Scalars['Float']>;
};

export type TopicConnection = {
  __typename?: 'TopicConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<TopicEdge>>;
};

export type TopicEdge = {
  __typename?: 'TopicEdge';
  node?: Maybe<Topic>;
  cursor: Scalars['String'];
};

export type TopicNodeSetConnection = {
  __typename?: 'TopicNodeSetConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<TopicNodeSetEdge>>;
  total_count?: Maybe<Scalars['Int']>;
  records?: Maybe<Scalars['Int']>;
};

export type TopicNodeSetEdge = {
  __typename?: 'TopicNodeSetEdge';
  node?: Maybe<Topic>;
  cursor: Scalars['String'];
};

export type LatestNoticeSubscriptionVariables = Exact<{
  arg1?: Maybe<Scalars['String']>;
  arg2?: Maybe<Scalars['String']>;
}>;


export type LatestNoticeSubscription = (
  { __typename?: 'Subscription' }
  & { latestnotice?: Maybe<(
    { __typename?: 'LatestNotice' }
    & Pick<LatestNotice, 'title'>
    & { notices?: Maybe<Array<Maybe<(
      { __typename?: 'Notice' }
      & { message?: Maybe<(
        { __typename?: 'Message' }
        & Pick<Message, 'subject' | 'message'>
      )> }
    )>>> }
  )> }
);


export const LatestNoticeDocument = gql`
    subscription latestNotice($arg1: String, $arg2: String) {
  latestnotice(arg1: $arg1, arg2: $arg2) {
    title
    notices {
      message {
        subject
        message
      }
    }
  }
}
    `;

/**
 * __useLatestNoticeSubscription__
 *
 * To run a query within a React component, call `useLatestNoticeSubscription` and pass it any options that fit your needs.
 * When your component renders, `useLatestNoticeSubscription` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the subscription, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useLatestNoticeSubscription({
 *   variables: {
 *      arg1: // value for 'arg1'
 *      arg2: // value for 'arg2'
 *   },
 * });
 */
export function useLatestNoticeSubscription(baseOptions?: ApolloReactHooks.SubscriptionHookOptions<LatestNoticeSubscription, LatestNoticeSubscriptionVariables>) {
        return ApolloReactHooks.useSubscription<LatestNoticeSubscription, LatestNoticeSubscriptionVariables>(LatestNoticeDocument, baseOptions);
      }
export type LatestNoticeSubscriptionHookResult = ReturnType<typeof useLatestNoticeSubscription>;
export type LatestNoticeSubscriptionResult = ApolloReactCommon.SubscriptionResult<LatestNoticeSubscription>;