import peasy.*;

PeasyCam cam;
int colorIndex = 1;
PVector cubePosition;
float cubeSize = 50;
PImage bluePenTexture;

void setup() {
  size(800, 600, P3D);
  cam = new PeasyCam(this, 200);
  perspective(PI/3.0, width/height, 2, 2000);
  cubePosition = new PVector(0, 0, 0);
}

void draw() {
  background(0);
  displayScene();
}

void displayScene() {
  pushMatrix();
  translate(cubePosition.x, cubePosition.y, cubePosition.z);
  
  switch (colorIndex) {
    case 1:
      bluePenTexture = loadImage("cuboMusical.png");
      applyTexture();
      break;
    case 2:
    bluePenTexture = loadImage("samba.png");
      applyTexture();
      break;
    case 3:
      bluePenTexture = loadImage("rap.png");
      applyTexture();
      break;
    case 4:
      bluePenTexture = loadImage("rock.png");
      applyTexture();
      break;
    case 5:
      bluePenTexture = loadImage("eletronica.png");
      applyTexture();
      break;
    case 6:
      bluePenTexture = loadImage("pop.png");
      applyTexture();
      break;
    case 7:
      bluePenTexture = loadImage("mpb.png");
      applyTexture();
      break;
    case 8:
      bluePenTexture = loadImage("bluepen.jpg");
      applyTexture();
      break;
  }
  drawColoredCube();
  popMatrix();
}

void applyTexture() {
  textureMode(NORMAL);
  beginShape(QUADS);
  texture(bluePenTexture);
  drawColoredCube();
  endShape();
}

void drawColoredCube() {
  noStroke();
  
  // Front face
  vertex(-cubeSize/2, -cubeSize/2, -cubeSize/2, 0, 0);
  vertex( cubeSize/2, -cubeSize/2, -cubeSize/2, 1, 0);
  vertex( cubeSize/2,  cubeSize/2, -cubeSize/2, 1, 1);
  vertex(-cubeSize/2,  cubeSize/2, -cubeSize/2, 0, 1);
  
  // Back face
  vertex(-cubeSize/2, -cubeSize/2,  cubeSize/2, 0, 0);
  vertex( cubeSize/2, -cubeSize/2,  cubeSize/2, 1, 0);
  vertex( cubeSize/2,  cubeSize/2,  cubeSize/2, 1, 1);
  vertex(-cubeSize/2,  cubeSize/2,  cubeSize/2, 0, 1);
  
  // Right face
  vertex( cubeSize/2, -cubeSize/2, -cubeSize/2, 0, 0);
  vertex( cubeSize/2, -cubeSize/2,  cubeSize/2, 1, 0);
  vertex( cubeSize/2,  cubeSize/2,  cubeSize/2, 1, 1);
  vertex( cubeSize/2,  cubeSize/2, -cubeSize/2, 0, 1);
  
  // Left face
  vertex(-cubeSize/2, -cubeSize/2, -cubeSize/2, 0, 0);
  vertex(-cubeSize/2, -cubeSize/2,  cubeSize/2, 1, 0);
  vertex(-cubeSize/2,  cubeSize/2,  cubeSize/2, 1, 1);
  vertex(-cubeSize/2,  cubeSize/2, -cubeSize/2, 0, 1);
  
  // Top face
  vertex(-cubeSize/2,  cubeSize/2, -cubeSize/2, 0, 0);
  vertex( cubeSize/2, cubeSize/2, -cubeSize/2, 1, 0);
  vertex( cubeSize/2, cubeSize/2, cubeSize/2, 1, 1);
  vertex(-cubeSize/2, cubeSize/2, cubeSize/2, 0, 1);

  // Bottom face
  vertex(-cubeSize/2, -cubeSize/2, -cubeSize/2, 0, 0);
  vertex( cubeSize/2, -cubeSize/2, -cubeSize/2, 1, 0);
  vertex( cubeSize/2, -cubeSize/2, cubeSize/2, 1, 1);
  vertex(-cubeSize/2, -cubeSize/2, cubeSize/2, 0, 1);
  
  if (colorIndex == 1) {
    endShape();
  }
}

void mouseClicked() {
  PVector mouse2D = new PVector(mouseX, mouseY);
  float screenCubeCenterX = screenX(cubePosition.x, cubePosition.y, cubePosition.z);
  float screenCubeCenterY = screenY(cubePosition.x, cubePosition.y, cubePosition.z);

  if (dist(mouse2D.x, mouse2D.y, screenCubeCenterX, screenCubeCenterY) <= cubeSize / 2) {
    colorIndex++;
    if (colorIndex > 8) {
      colorIndex = 1;
    }
  }
}
