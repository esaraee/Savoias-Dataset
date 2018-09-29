# SAVOIAS Dataset
we introduce SAVOIAS a visual complexity dataset that compromises of more than 1,400 images from seven image categories
namely **Scenes**, **Advertisements**, **Visualization and infographics**, **Objects**, **Interior design**,
**Art**, and **Suprematism**. The images in each category portray diverse characteristics including various low-level and high-level features, objects, backgrounds, textures and patterns, text, and graphics. The ground truth for SAVOIAS is obtained by crowdsourcing more than 37,000 pairwise comparisons of images using the forced-choice methodology and with more than 1,600
contributors. The resulting relative scores are then converted to absolute visual complexity scores using the Bradley-Terry
method and matrix completion. When applying five state-of-the-art algorithms to analyze the visual complexity of the images
in the SAVOIAS dataset, we found that the scores obtained from these baseline tools only correlate well with crowd-sourced
labels for abstract patterns in the Suprematism category (Pearson correlation r=0.84). For the other categories, 
in particular, the objects and advertisement categories, low correlation coefficients were revealed (r=0.3 and 0.56,
respectively). These findings suggest that (1) state-of-the-art approaches are mostly insufficient and (2) SAVOIAS enables
category-specific method development, which is likely to improve the impact of visual complexity analysis on specific
application areas, including computer vision.

### Baseline Comparison for SAVOIAS Dataset

![alt text](https://raw.githubusercontent.com/esaraee/Savoias-Dataset/master/baselines.png)

### Image Samples from SAVOIAS Dataset

![alt text](https://raw.githubusercontent.com/esaraee/Savoias-Dataset/master/SAVOIAS-image-samples.png)


## Acknowledgement

This work was supported in part by [NSF (1421943)](https://nsf.gov/awardsearch/showAward?AWD_ID=1421943) and [NSF (1838193)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1838193&HistoricalAwards=false). We would also like to thank the students, [Yifu Hu](http://cs-people.bu.edu/yfhu) and [Yi Zheng](http://cs-people.bu.edu/yizheng/) who prepared the images for the interior design category of our dataset.

## Credits

[Elham Saraee](http://cs-people.bu.edu/esaraee/), [Mona Jalal](http://monajalal.com), [Margrit Betke](http://www.cs.bu.edu/~betke/)




