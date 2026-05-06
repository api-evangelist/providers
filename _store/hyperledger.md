---
aid: hyperledger
name: Hyperledger
description: Hyperledger is an open source collaborative effort created to advance cross-industry blockchain technologies, originally hosted under the Linux Foundation and now stewarded by LF Decentralized Trust. It hosts enterprise-grade blockchain frameworks including Fabric, Besu, Indy, Iroha, and Cacti, along with tools like Firefly and Caliper for blockchain development, identity, and operations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Blockchain
  - Distributed Ledger
  - Enterprise
  - Linux Foundation
  - Smart Contracts
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/hyperledger/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: hyperledger:hyperledger-besu-api
    name: Hyperledger Besu API
    description: Hyperledger Besu is an Ethereum client written in Java exposing JSON-RPC APIs for blockchain interaction including admin, debug, eth, net, web3, txpool, miner, and trace namespaces.
    humanURL: https://besu.hyperledger.org/
    baseURL: https://besu.example.com
    tags:
      - Blockchain
      - Ethereum
      - Json-Rpc
      - Smart Contracts
    properties:
      - type: Documentation
        url: https://besu.hyperledger.org/public-networks/reference/api
      - type: GitHub
        url: https://github.com/hyperledger/besu
      - type: OpenAPI
        url: openapi/hyperledger-openapi.yml
  - aid: hyperledger:hyperledger-fabric-api
    name: Hyperledger Fabric API
    description: Hyperledger Fabric is a permissioned distributed ledger platform. Programmatic access is provided via the Fabric Gateway, peer gRPC APIs, and SDKs for chaincode invocation, ledger queries, and channel administration.
    humanURL: https://hyperledger-fabric.readthedocs.io/
    tags:
      - Blockchain
      - Distributed Ledger
      - Permissioned
      - Smart Contracts
    properties:
      - type: Documentation
        url: https://hyperledger-fabric.readthedocs.io/en/latest/
      - type: GatewayDocs
        url: https://hyperledger.github.io/fabric-gateway/
      - type: GitHub
        url: https://github.com/hyperledger/fabric
  - aid: hyperledger:hyperledger-firefly-api
    name: Hyperledger FireFly API
    description: Hyperledger FireFly is a multiparty system orchestration framework providing REST APIs for tokens, messages, identities, contracts, and events across multiple blockchain protocols.
    humanURL: https://hyperledger.github.io/firefly/
    tags:
      - Blockchain
      - Multiparty
      - Tokens
      - Web3
    properties:
      - type: Documentation
        url: https://hyperledger.github.io/firefly/latest/reference/api/
      - type: GitHub
        url: https://github.com/hyperledger/firefly
  - aid: hyperledger:hyperledger-indy-api
    name: Hyperledger Indy API
    description: Hyperledger Indy provides tools, libraries, and reusable components for decentralized identities rooted on blockchains. APIs are exposed via the Indy SDK and Indy Node REST endpoints.
    humanURL: https://www.hyperledger.org/projects/hyperledger-indy
    tags:
      - Decentralized Identity
      - Did
      - Identity
      - Self-Sovereign Identity
    properties:
      - type: Documentation
        url: https://hyperledger-indy.readthedocs.io/
      - type: GitHub
        url: https://github.com/hyperledger/indy-node
  - aid: hyperledger:hyperledger-cacti-api
    name: Hyperledger Cacti API
    description: Hyperledger Cacti (formerly Cactus) is a pluggable enterprise-grade framework for cross-chain transactions, providing connector plugins and REST APIs for interoperability across DLTs.
    humanURL: https://hyperledger-cacti.github.io/cacti/
    tags:
      - Blockchain
      - Interoperability
      - Cross-Chain
    properties:
      - type: Documentation
        url: https://hyperledger-cacti.github.io/cacti/
      - type: GitHub
        url: https://github.com/hyperledger/cacti
common:
  - type: Documentation
    name: Hyperledger Documentation
    url: https://www.hyperledger.org/use
  - type: LFDecentralizedTrust
    name: LF Decentralized Trust
    url: https://lfdecentralizedtrust.org/
  - type: GitHubOrg
    name: Hyperledger GitHub
    url: https://github.com/hyperledger
  - type: LFDTGitHub
    name: LF Decentralized Trust GitHub
    url: https://github.com/LF-Decentralized-Trust
  - type: Wiki
    url: https://wiki.lfdecentralizedtrust.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
