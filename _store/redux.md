---
aid: redux
name: Redux
description: Redux is a predictable state container for JavaScript apps. It helps write applications that behave consistently, run in different environments (client, server, and native), and are easy to test. Redux provides a single immutable state tree, pure reducer functions for state transitions, and a unidirectional data flow pattern based on the Flux architecture. The Redux ecosystem includes React Redux for React bindings, Redux Toolkit for simplified development patterns, and Redux DevTools for time-travel debugging. Redux is widely used with React but can be paired with any JavaScript view library.
type: Index
image: https://redux.js.org/img/redux-logo-landscape.png
url: https://raw.githubusercontent.com/api-evangelist/redux/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Flux Architecture
  - Frontend
  - Javascript
  - Predictable State
  - React
  - State Management
  - Typescript
apis:
  - name: Redux Core API
    description: Core Redux library for managing application state through a predictable unidirectional data flow. The library exposes createStore, combineReducers, applyMiddleware, compose, and bindActionCreators as its primary API surface. State mutations are triggered by dispatching plain action objects to a store, which processes them through pure reducer functions to produce the next immutable state tree.
    image: https://redux.js.org/img/redux-logo-landscape.png
    baseURL: https://redux.js.org
    humanURL: https://redux.js.org
    tags:
      - Actions
      - Middleware
      - Reducers
      - State Management
      - Store
    properties:
      - type: Documentation
        url: https://redux.js.org/introduction/getting-started
      - type: ApiReference
        url: https://redux.js.org/api/api-reference
      - type: GitHubRepository
        url: https://github.com/reduxjs/redux
      - type: NpmPackage
        url: https://www.npmjs.com/package/redux
      - type: TypeScript
        url: https://redux.js.org/usage/usage-with-typescript
      - type: Changelog
        url: https://github.com/reduxjs/redux/releases
      - type: License
        url: https://github.com/reduxjs/redux/blob/master/LICENSE.md
  - name: React Redux API
    description: Official React bindings for Redux, enabling React components to interact with a Redux store. Provides hooks (useSelector, useDispatch, useStore) and a Provider component for connecting the Redux store to the React component tree. React Redux ensures that components only re-render when the pieces of state they subscribe to change.
    image: https://react-redux.js.org/img/redux-logo-landscape.png
    baseURL: https://react-redux.js.org
    humanURL: https://react-redux.js.org
    tags:
      - Bindings
      - Components
      - Hooks
      - React
      - State Management
    properties:
      - type: Documentation
        url: https://react-redux.js.org/introduction/getting-started
      - type: ApiReference
        url: https://react-redux.js.org/api/hooks
      - type: GitHubRepository
        url: https://github.com/reduxjs/react-redux
      - type: NpmPackage
        url: https://www.npmjs.com/package/react-redux
      - type: Tutorials
        url: https://react-redux.js.org/tutorials/quick-start
      - type: Changelog
        url: https://github.com/reduxjs/react-redux/releases
  - name: Redux Toolkit API
    description: The official, opinionated, batteries-included toolset for efficient Redux development. Redux Toolkit simplifies common Redux use cases including store setup, creating reducers and writing immutable update logic, and creating entire state slices at once. Includes configureStore, createSlice, createAsyncThunk, createEntityAdapter, and the RTK Query data fetching and caching solution.
    image: https://redux-toolkit.js.org/img/redux-logo-landscape.png
    baseURL: https://redux-toolkit.js.org
    humanURL: https://redux-toolkit.js.org
    tags:
      - Code Generation
      - Immer
      - Redux Toolkit
      - Rtk Query
      - Simplified Redux
      - Toolkit
    properties:
      - type: Documentation
        url: https://redux-toolkit.js.org/introduction/getting-started
      - type: ApiReference
        url: https://redux-toolkit.js.org/api/configureStore
      - type: GitHubRepository
        url: https://github.com/reduxjs/redux-toolkit
      - type: NpmPackage
        url: https://www.npmjs.com/package/@reduxjs/toolkit
      - type: RtkQuery
        url: https://redux-toolkit.js.org/rtk-query/overview
      - type: Tutorials
        url: https://redux-toolkit.js.org/tutorials/quick-start
      - type: Changelog
        url: https://github.com/reduxjs/redux-toolkit/releases
  - name: Redux DevTools API
    description: Developer tools for debugging Redux applications with time-travel debugging capabilities. The Redux DevTools Extension allows inspection of every state and action payload dispatched, going back in time by cancelling actions, and replaying state changes. Also available as a standalone NPM package for programmatic integration.
    image: https://github.com/reduxjs/redux-devtools/raw/main/extension/docs/design/logo.png
    baseURL: https://github.com/reduxjs/redux-devtools
    humanURL: https://github.com/reduxjs/redux-devtools
    tags:
      - Browser Extension
      - Debugging
      - Devtools
      - Time Travel
    properties:
      - type: Documentation
        url: https://github.com/reduxjs/redux-devtools/blob/main/README.md
      - type: GitHubRepository
        url: https://github.com/reduxjs/redux-devtools
      - type: ChromeExtension
        url: https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd
      - type: FirefoxExtension
        url: https://addons.mozilla.org/en-US/firefox/addon/reduxdevtools/
      - type: NpmPackage
        url: https://www.npmjs.com/package/redux-devtools
  - name: Redux Saga
    description: A Redux middleware library that aims to make application side effects such as asynchronous data fetching and accessing browser caches easier to manage and more efficient to execute. Uses ES6 Generators to make async flows easy to read, write, and test.
    humanURL: https://redux-saga.js.org
    baseURL: https://redux-saga.js.org
    tags:
      - Async
      - Generators
      - Middleware
      - Side Effects
    properties:
      - type: Documentation
        url: https://redux-saga.js.org/docs/introduction/GettingStarted
      - type: GitHubRepository
        url: https://github.com/redux-saga/redux-saga
      - type: NpmPackage
        url: https://www.npmjs.com/package/redux-saga
  - name: Redux Observable
    description: RxJS-based middleware for Redux. Compose and cancel async actions to create side effects and more using Epics. An epic is a function which takes a stream of actions and returns a stream of actions.
    humanURL: https://redux-observable.js.org
    baseURL: https://redux-observable.js.org
    tags:
      - Middleware
      - Observables
      - Reactive
      - Rxjs
    properties:
      - type: Documentation
        url: https://redux-observable.js.org/docs/basics/Epics.html
      - type: GitHubRepository
        url: https://github.com/redux-observable/redux-observable
      - type: NpmPackage
        url: https://www.npmjs.com/package/redux-observable
  - name: Redux Thunk
    description: Thunk middleware for Redux, included by default with Redux Toolkit. Allows writing action creators that return a function instead of an action object, enabling delayed dispatch and conditional dispatch based on current state.
    humanURL: https://github.com/reduxjs/redux-thunk
    baseURL: https://github.com/reduxjs/redux-thunk
    tags:
      - Async
      - Middleware
      - Thunk
    properties:
      - type: Documentation
        url: https://github.com/reduxjs/redux-thunk#readme
      - type: GitHubRepository
        url: https://github.com/reduxjs/redux-thunk
      - type: NpmPackage
        url: https://www.npmjs.com/package/redux-thunk
  - name: Reselect
    description: A selector library for Redux. Selectors are functions that compute derived data from the Redux state, allowing Redux to store the minimal possible state. Reselect creates memoized selector functions that recompute only when their inputs change.
    humanURL: https://github.com/reduxjs/reselect
    baseURL: https://github.com/reduxjs/reselect
    tags:
      - Memoization
      - Performance
      - Selectors
    properties:
      - type: Documentation
        url: https://reselect.js.org/
      - type: GitHubRepository
        url: https://github.com/reduxjs/reselect
      - type: NpmPackage
        url: https://www.npmjs.com/package/reselect
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://redux.js.org
  - type: GitHubOrganization
    url: https://github.com/reduxjs
  - type: Blog
    url: https://blog.isquaredsoftware.com/
  - type: Community
    url: https://discord.gg/redux
  - type: Twitter
    url: https://twitter.com/reduxjs
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/redux
  - type: StyleGuide
    url: https://redux.js.org/style-guide/style-guide
  - type: Faq
    url: https://redux.js.org/faq
  - type: Tutorials
    url: https://redux.js.org/tutorials/essentials/part-1-overview-concepts
  - type: License
    url: https://github.com/reduxjs/redux/blob/master/LICENSE.md
  - type: JSONSchema
    url: json-schema/redux-store-schema.json
  - type: JSONSchema
    url: json-schema/redux-action-schema.json
  - type: JSONStructure
    url: json-structure/redux-store-structure.json
  - type: JSONLDContext
    url: json-ld/redux-context.jsonld
  - type: Vocabulary
    url: vocabulary/redux-vocabulary.yml
---
