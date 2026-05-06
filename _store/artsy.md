---
aid: artsy
name: Artsy
description: Artsy is the world's largest online art marketplace, connecting collectors with artists and galleries worldwide. The platform features over 1 million artworks from 100,000+ artists and provides access to galleries, art fairs, and auction houses globally. Artsy offers a Public API providing access to images of historic artwork and related information for educational and non-commercial purposes, with access limited to public domain works. The API provides resources for artists, artworks, galleries, shows, sales, and gene (classification) data. Note that the public API may be retired; partner integrations are handled through a separate partner API program.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Art
  - Marketplace
  - Artists
  - Collectors
  - Galleries
created: '2025-02-24'
modified: '2026-04-19'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/artsy/refs/heads/main/apis.yml
apis:
  - aid: artsy:artsy-api
    name: Artsy Public API
    description: The Artsy Public API provides access to images of historic artwork and related information on artsy.net for educational and non-commercial purposes. Resources include artists, artworks, editions, fairs, genes (art classification taxonomy), images, shows, collections, partners, profiles, search, sales, bids, and bidder positions.
    humanURL: https://developers.artsy.net/
    baseURL: https://api.artsy.net/api
    tags:
      - Art
      - Artists
      - Artwork
      - Galleries
      - Search
    properties:
      - type: Documentation
        url: https://developers.artsy.net/v2
      - type: GettingStarted
        url: https://developers.artsy.net/v2/docs/authentication
      - type: Authentication
        url: https://developers.artsy.net/v2/docs/authentication
common:
  - type: Portal
    url: https://www.artsy.net/
    title: Artsy Website
  - type: Documentation
    url: https://developers.artsy.net/
    title: Developer Documentation
  - type: Blog
    url: https://artsy.github.io/
    title: Engineering Blog
  - type: GitHubOrganization
    url: https://github.com/artsy
    title: Artsy GitHub Organization
  - type: SignUp
    url: https://www.artsy.net/signup
    title: Sign Up
  - type: Login
    url: https://www.artsy.net/login
    title: Login
  - type: Features
    data:
      - name: Artist and Artwork Data
        description: Comprehensive database of artist biographies, artwork metadata, images, dimensions, medium, and provenance for over 1 million artworks.
      - name: Gallery and Show Data
        description: Access to gallery profiles, exhibition shows, art fairs, and partner information from Artsy's global gallery network.
      - name: Art Classification Genes
        description: Artsy's proprietary gene taxonomy for classifying artworks by style, period, subject matter, and medium, enabling sophisticated art discovery and recommendation.
      - name: Auction and Sales Data
        description: Sale, bidder, and bid information for auction and buy-now listings on the Artsy platform.
      - name: Full-Text Search
        description: Search across artists, artworks, galleries, and other art world entities with faceted filtering and relevance ranking.
  - type: UseCases
    data:
      - name: Art Education Applications
        description: Educational platforms use the Artsy API to access public domain artwork images and artist information for art history curriculum and museum education tools.
      - name: Gallery Integration
        description: Partner galleries integrate with the Artsy Partner API to manage artwork listings, track collector inquiries, and access sales analytics.
      - name: Art Discovery Tools
        description: Developers build art recommendation and discovery applications using Artsy's gene taxonomy and artist relationship data.
      - name: Research and Analysis
        description: Art market researchers access Artsy data to analyze trends, auction results, and artist career trajectories.
  - type: Integrations
    data:
      - name: Artsy Partner Program
        description: Gallery and auction house partners integrate directly with Artsy through the Partner API for full marketplace integration including artwork listings and collector communications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
