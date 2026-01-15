var handler = document.querySelector('.handler');
var wrapper = handler.closest('.wrapper');
var box_left = wrapper.querySelector('.left');
var box_right = wrapper.querySelector('.right');
var isHandlerDragging = false;

document.addEventListener('mousedown', function(e) {
  // If mousedown event is fired from .handler, toggle flag to true
  if (e.target === handler) {
    isHandlerDragging = true;
  }
});

document.addEventListener('mousemove', function(e) {
  // Don't do anything if dragging flag is false
  if (!isHandlerDragging) {
    return false;
  }

  // Get offset
  var containerOffsetLeft = wrapper.offsetLeft;

  // Get x-coordinate of pointer relative to container
  var pointerRelativeXpos = e.clientX - containerOffsetLeft;
  
  // Arbitrary minimum width set on box A, otherwise its inner content will collapse to width of 0
  var boxAminWidth = 210;
  var boxAmaxWidth = 400;

  // Resize box A
  // * 8px is the left/right spacing between .handler and its inner pseudo-element
  // * Set flex-grow to 0 to prevent it from growing
  box_left.style.width = (Math.min(Math.max(boxAminWidth, pointerRelativeXpos),boxAmaxWidth)) + 'px';
  box_left.style.flexGrow = 0;
  box_right.style.left = (Math.min(Math.max(boxAminWidth, pointerRelativeXpos),boxAmaxWidth)* (20/18)) + 'px';
  box_right.style.flexGrow = 0;
  handler.style.marginLeft = box_left.style.width;
});

document.addEventListener('mouseup', function(e) {
  // Turn off dragging flag when user mouse is up
  isHandlerDragging = false;
});
