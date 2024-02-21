class Board extends ReadableByteStreamController.Component{
    renderSquare(i) {
        return <Square value={i} />;  
    }
}