import React from 'react'
import "./Main.css";
import Webcam from 'react-webcam'

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: "user"
  };
  
const WebcamCapture = () => {
const webcamRef = React.useRef(null);
const capture = React.useCallback(
    () => {
    const imageSrc = webcamRef.current.getScreenshot();
    },
    [webcamRef]
);
return (
    <>
    <Webcam
        audio={false}
        height={720}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={1280}
        videoConstraints={videoConstraints}
    />
    <button onClick={capture}>Capture photo</button>
    </>
    );
  };

  const WebcamCaptureG = () => {
    const webcamRef = React.useRef(null);
    const capture = React.useCallback(
      () => {
        const imageSrc = webcamRef.current.getScreenshot();
      },
      [webcamRef]
    );
    return (
      <>
        <Webcam
          audio={false}
          height={720}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={1280}
          videoConstraints={videoConstraints}
        />
        <button onClick={capture}>Capture photo</button>
      </>
    );
  };


function Main() {
  return (
    <div className='body'>
        <Webcam/>
        <button onClick= {WebcamCaptureG()}>
            Captura de objeto
        </button>
      Objeto detectado:
      
    </div>
  )
}

export default Main
