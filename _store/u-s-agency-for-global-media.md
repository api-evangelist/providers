---
aid: u-s-agency-for-global-media
url: https://raw.githubusercontent.com/api-evangelist/u-s-agency-for-global-media/refs/heads/main/apis.yml
apis:
  - aid: u-s-agency-for-global-media:u-s-agency-for-global-media
    name: U.S. Agency for Global Media
    tags:
      - Federal Government
      - Media
      - Broadcasting
      - International
    humanURL: https://www.usagm.gov/
    properties:
      - url: https://www.usagm.gov/
        type: Documentation
      - url: https://www.usagm.gov/who-we-are/
        type: About
      - url: https://www.usagm.gov/networks/
        type: Documentation
        title: Networks and Outlets
    description: The United States Agency for Global Media (USAGM) is an independent federal agency that oversees a network of media organizations providing news and information to audiences around the world in support of freedom and democracy. USAGM oversees Voice of America (VOA), Radio Free Europe/Radio Liberty (RFE/RL), Radio Free Asia (RFA), Office of Cuba Broadcasting (OCB), Middle East Broadcasting Networks (MBN), and the Open Technology Fund (OTF). Together these entities reach approximately 427 million people weekly in 64 languages.
  - aid: u-s-agency-for-global-media:usagm-press-freedom
    name: USAGM Press Freedom
    tags:
      - Press Freedom
      - Media
      - Open Data
    humanURL: https://github.com/usagm/usagm-press-freedom
    properties:
      - url: https://github.com/usagm/usagm-press-freedom
        type: GitHubRepository
    description: USAGM press freedom data and resources published on GitHub.
  - aid: u-s-agency-for-global-media:open-technology-fund
    name: Open Technology Fund
    tags:
      - Internet Freedom
      - Privacy
      - Security
      - Open Source
    humanURL: https://www.opentech.fund/
    properties:
      - url: https://www.opentech.fund/
        type: Documentation
      - url: https://github.com/usagm/internet-freedom
        type: GitHubRepository
        title: Internet Freedom Resources
    description: The Open Technology Fund (OTF) is a U.S. government-funded independent nonprofit that supports the development of open-source internet freedom technologies to advance human rights and open societies. OTF funds projects like Tor, Signal, and other privacy and circumvention tools that help individuals in repressive environments access a free and open internet.
name: U.S. Agency for Global Media
tags:
  - Federal Government
  - Media
  - Broadcasting
  - International
  - Press Freedom
  - Internet Freedom
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-05-03'
position: Consuming
description: The U.S. Agency for Global Media (USAGM) is an independent federal agency that oversees a network of international media organizations aimed at providing news and information to audiences around the world in support of freedom and democracy. These media outlets include Voice of America (VOA), Radio Free Europe/Radio Liberty (RFE/RL), Radio Free Asia (RFA), Office of Cuba Broadcasting (OCB), Middle East Broadcasting Networks (MBN), and the Open Technology Fund (OTF). Together these entities operate in over 64 languages and reach approximately 427 million people weekly, producing more than 3,000 hours of original programming per week in regions where access to a free press is limited.
common:
  - type: Website
    url: https://www.usagm.gov/
  - type: About
    url: https://www.usagm.gov/who-we-are/
  - type: GitHubOrganization
    url: https://github.com/usagm
  - type: Features
    data:
      - name: Voice of America (VOA)
        description: The largest U.S. international broadcaster, providing news and information in 47 languages to audiences in regions underserved by free press, including sub-Saharan Africa, Latin America, and Asia.
      - name: Radio Free Europe/Radio Liberty (RFE/RL)
        description: Broadcasts domestic news coverage to audiences in Central and Eastern Europe, Russia, the Caucasus, Central Asia, and the Middle East in 27 languages.
      - name: Radio Free Asia (RFA)
        description: Provides uncensored news and information in nine languages to audiences across East and Southeast Asia, including China, North Korea, Vietnam, and Burma.
      - name: Middle East Broadcasting Networks (MBN)
        description: Delivers Arabic-language television and digital content across the Middle East and North Africa, including Alhurra TV and Radio Sawa.
      - name: Open Technology Fund (OTF)
        description: Funds the development of open-source internet freedom tools and technologies that help individuals in repressive environments access a free and open internet.
      - name: Internet Freedom Programs
        description: Anti-censorship, circumvention, and digital safety programs supporting journalists, activists, and ordinary citizens operating in restricted environments.
  - type: UseCases
    data:
      - name: International News Delivery
        description: Delivering independent, accurate news and information to audiences in countries that lack a free press or face government-controlled media.
      - name: Press Freedom Advocacy
        description: Supporting journalists and media organizations operating in repressive environments by providing training, tools, and reporting support.
      - name: Internet Circumvention
        description: Enabling internet users in censored environments to bypass restrictions and access uncensored online content through funded circumvention tools.
      - name: Digital Safety
        description: Protecting journalists and activists with digital security tools and training through Open Technology Fund-supported projects.
      - name: Media Development
        description: Supporting the development of independent media ecosystems in transitioning democracies through training, technology, and partnerships.
  - type: Integrations
    data:
      - name: Tor Project
        description: OTF-funded privacy and anonymity network enabling secure communication for users in censored or surveilled environments.
      - name: Signal
        description: End-to-end encrypted messaging platform supported by OTF for secure communications by journalists and activists.
      - name: Open Whisper Systems
        description: Developer of Signal protocol providing encrypted messaging and calling for vulnerable populations worldwide.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/u-s-agency-for-global-media/refs/heads/main/vocabulary/u-s-agency-for-global-media-vocabulary.yaml
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/u-s-agency-for-global-media/refs/heads/main/json-ld/u-s-agency-for-global-media-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
