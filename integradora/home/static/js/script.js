const galleryContainer = document.querySelector('.gallery-container');
const galleryItems = document.querySelectorAll('.gallery-item');

class Carousel {
    constructor(container, items) {
        this.carouselContainer = container;
        this.carouselArray = [...items];
        this.intervalTime = 3000;
        console.log("Carousel initialized:", this.carouselArray); 
    }

    updateGallery() {
        console.log("Updating gallery...");

       
        this.carouselArray.forEach(el => {
            el.classList.remove('gallery-item-1', 'gallery-item-2', 'gallery-item-3', 'gallery-item-4', 'gallery-item-5');
        });

        
        this.carouselArray.slice(0, 5).forEach((el, i) => {
            el.classList.add(`gallery-item-${i + 1}`);
        });

        console.log("Gallery updated:", this.carouselArray); 
    }

    setCurrentState() {
       
        this.carouselArray.push(this.carouselArray.shift());

        this.updateGallery();
    }

    startAutoSlide() {
        
        setInterval(() => {
            this.setCurrentState();
        }, this.intervalTime); 
    }
}

const exampleCarousel = new Carousel(galleryContainer, galleryItems);

exampleCarousel.startAutoSlide(); 
