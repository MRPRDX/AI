import csv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import glob

# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='face_landmarker_v2_with_blendshapes.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       output_facial_transformation_matrixes=True,
                                       num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)


def dis(d, f):
    distance = ((d.x - f.x) ** 2 + (d.y - f.y) ** 2) ** 0.5
    return distance


paths = glob.glob("D:/Desktop/Dataset/MAR/no_yawn/*")


def EAR_pipeline(paths):
    with open('no Yawn.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["left_EAR", "right_EAR", "MAR", "Label"])
        for item in paths:
            try:
                image = mp.Image.create_from_file(item)
                detection_result = detector.detect(image)
                # EAR Nodes
                # node_160 = detection_result.face_landmarks[0][160]
                # node_144 = detection_result.face_landmarks[0][144]
                # node_33 = detection_result.face_landmarks[0][33]
                # node_133 = detection_result.face_landmarks[0][133]
                # node_153 = detection_result.face_landmarks[0][153]
                # node_158 = detection_result.face_landmarks[0][158]
                # node_385 = detection_result.face_landmarks[0][385]
                # node_380 = detection_result.face_landmarks[0][380]
                # node_362 = detection_result.face_landmarks[0][362]
                # node_263 = detection_result.face_landmarks[0][263]
                # node_373 = detection_result.face_landmarks[0][373]
                # node_387 = detection_result.face_landmarks[0][387]
                # MAR Nodes
                node_160 = detection_result.face_landmarks[0][160]
                node_78 = detection_result.face_landmarks[0][78]
                node_308 = detection_result.face_landmarks[0][308]
                node_303 = detection_result.face_landmarks[0][303]
                node_404 = detection_result.face_landmarks[0][404]
                node_16 = detection_result.face_landmarks[0][16]
                node_11 = detection_result.face_landmarks[0][11]
                node_73 = detection_result.face_landmarks[0][73]
                node_180 = detection_result.face_landmarks[0][180]
                p73180 = dis(node_73, node_180)
                p78308 = dis(node_78, node_308)
                p1116 = dis(node_11, node_16)
                p303404 = dis(node_303, node_404)
                MAR = (p73180 + p1116 + p303404) / (2 * p78308)
                # p26l = dis(node_144, node_160)
                # p35l = dis(node_158, node_153)
                # p14l = dis(node_33, node_133)
                # p26r = dis(node_385, node_380)
                # p35r = dis(node_373, node_387)
                # p14r = dis(node_362, node_263)
                # left_EAR = (p26l + p35l) / (2 * p14l)
                # right_EAR = (p26r + p35r) / (2 * p14r)
                writer.writerow([MAR, 0])
            except Exception:
                pass


EAR_pipeline(paths)
