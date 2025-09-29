# cherrybomb
A capable desktop application for data scraping from social media platforms and other OSINT sources.

Cherrybomb is intended to be used by ethical hackers, data scientists, machine learning engineers and other developers, researchers and people who require large amounts of data from social media platforms (or other websites).

The makers and contributors of cherrbomb and any of its related projects do not condone or endore the malicious or violent use of this software. Tools like cherrybomb are being developed with the intent of helping scientists, researchers and developers better understand the relation people have with technology, how they interact using it, and how we can use this data to make informed decisions and train capable machine learning models to assist everyone. Usage of these tools for malicious purposes such as (but not limited to) exploitation, blackmail, threatening, stalking or other similar things is frankly, disgusting.

## Using cherrybomb

Currently cherrbomb is in an early stage of development, wherein builds should be expected to have bugs or not even function at all.

If you feel like this is a project you value and you would like to contribute, please make a pull request with your suggested changes. I don't have super specific rules for PRs, I just want to see what you can do and improve the application by any means possible.

## Development setup

This section is yet to be written.

## Tech Stack

### Application
The intent for this application is to use C++ and WebView for the main user interface. This allows the use of more complex rendering tools like OpenCL/OpenGL/WebGL/etc. to render interactive graphs and tools for data visualization.

### Backend

The backend functionality (i.e. the scraping) of the application is intended to be written using Python and possibly some custom components in TypeScript or Python. Ideally existing APIs for platforms will be used to reduce the amount of new code required, but naturally some of the existing libraries may be broken or require updating to function with existing services.

Ideally cherrybomb will be a paid service, which restricts the application to using unofficial or free APIs available to the general public. For platforms like Twitter/X, this can cause issues due to the heavy emphasis on the paid API. Other platforms like Instagram do not provide official APIs for scraping information or for extracting user information, mainly for privacy reasons (probably). This means we will need to use unofficial APIs to even have the functionality in the application.

Due to the unstable nature of unofficial APIs, this means that the application cannot guarantee functionality for any unofficial platform, ever.

### Documentation

Documentation for the program will be done using Doxygen, which supports C++ code very well and has some workarounds for Python based code. TypeScript code will be documented using TypeDoc.


