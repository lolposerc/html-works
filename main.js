const car = {};

car.brand = 'Toyota';
car.model = 'Camry';
car.year = 2021;
car.isEngineOn = false;

car.startEngine = function() {
    this.isEngineOn = true;
    console.log(`Двигатель ${this.brand} ${this.model} запущен.`);
};

car.stopEngine = function() {
    this.isEngineOn = false;
    console.log(`Двигатель ${this.brand} ${this.model} заглушен.`);
};