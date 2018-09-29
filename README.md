# SAVOIAS Dataset

we introduce **SAVOIAS** a visual complexity dataset that compromises of more than 1,400 images from seven image categories
namely [**Scenes**](http://places2.csail.mit.edu/), [**Advertisements**](http://people.cs.pitt.edu/~kovashka/ads/), [**Visualization and infographics**](http://massvis.mit.edu/), [**Objects**](http://cocodataset.org/#home), **Interior design**,
[**Art**](https://github.com/BathVisArtData/PeopleArt), and [**Suprematism**](https://github.com/BathVisArtData/PeopleArt/tree/master/JPEGImages/Suprematism). The images in each category portray diverse characteristics including various low-level and high-level features, objects, backgrounds, textures and patterns, text, and graphics. The ground truth for SAVOIAS is obtained by crowdsourcing more than 37,000 pairwise comparisons of images using the forced-choice methodology and with more than 1,600
contributors using the [Figure-Eight](http://figure-eight.com/) crowdplatform. The resulting relative scores are then converted to absolute visual complexity scores using the Bradley-Terry
method and matrix completion. When applying five state-of-the-art algorithms to analyze the visual complexity of the images
in the SAVOIAS dataset, we found that the scores obtained from these baseline tools only correlate well with crowd-sourced
labels for abstract patterns in the Suprematism category (Pearson correlation r=0.84). For the other categories, 
in particular, the objects and advertisement categories, low correlation coefficients were revealed (r=0.3 and 0.56,
respectively). These findings suggest that (1) state-of-the-art approaches are mostly insufficient and (2) SAVOIAS enables
category-specific method development, which is likely to improve the impact of visual complexity analysis on specific
application areas, including computer vision.

## Usage

git clone the repositoty:
```
git clone https://github.com/esaraee/Savoias-Dataset.git
```
1420 images of the SAVOIAS dataset are located in the respective 7 categories the belong to in **Images** folder. In addition, if researchers are interested to find the original name of the images they can use the Name_Mapping folder to retreive those. The visual complexity ground-truth scores for the SAVOIAS images is located in **Ground truth** folder. 


### Baseline Comparison for SAVOIAS Dataset

![alt text](https://raw.githubusercontent.com/esaraee/Savoias-Dataset/master/baselines.png)

### Image Samples from SAVOIAS Dataset

![alt text](https://raw.githubusercontent.com/esaraee/Savoias-Dataset/master/SAVOIAS-image-samples.png)


## Getting help

If you have any question, concern, or bug report, please file an issue in this repository's Issue Tracker and we will respond accordingly.

## Funding
This research was partially funded by the following NSF Awards:

- [NSF Award #1421943](https://nsf.gov/awardsearch/showAward?AWD_ID=1421943) RI: Small: Using Humans in the Loop to Collect High-quality Annotations from Images and Time-lapse Videos of Cells
- [NSF Award #1838193](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1838193&HistoricalAwards=false) BIGDATA: IA: Multiplatform, Multilingual, and Multimodal Tools for Analyzing Public Communication in over 100 Languages

## Acknowledgement

We would like to thank the students, [Yifu Hu](http://cs-people.bu.edu/yfhu) and [Yi Zheng](http://cs-people.bu.edu/yizheng/) who prepared the images for the interior design category of our dataset.

## Citation

Please cite the following paper in your publications if it helps you with your research.
```
@inproceedings{SaraeeJaBe19,
  author    = {Elham Saraee and
               Mona Jalal and
               Margrit Betke},
  title     = {SAVOIAS: A Diverse, Multi-Category Visual Complexity Dataset},
  booktitle = {2019 {IEEE} Winter Conference on Applications of Computer Vision,
               {WACV} 2018, Waikoloa Village, HI, USA, Jan 8-10, 2019},
  year      = {2019}
}
```

## License

SAVOIAS dataset is freely and publicly available under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Story Behind Naming
Savoia is a region in Italy. Here is a beautiful picture of Salt crystal in salt brine, salt production at Margherita di Savoia, Apulia, Italy by Franz Aberham via Getty Images. 
![alt text][https://raw.githubusercontent.com/esaraee/Savoias-Dataset/master/savoia.jpg]


## Credits

[Elham Saraee](http://cs-people.bu.edu/esaraee/), [Mona Jalal](http://monajalal.com), [Margrit Betke](http://www.cs.bu.edu/~betke/)





